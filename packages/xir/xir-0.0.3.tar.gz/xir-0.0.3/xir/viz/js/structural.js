function runviz(d3, width, height) {

  ///
  /// Helpers
  ///
  const concat = (x,y) =>
    x.concat(y)

  const flatmap = (xs, f) =>
    xs.map(f).reduce(concat, [])


  ///
  /// Raw Data
  ///

  var raw_data = $data;
  console.log(raw_data);

  ///
  /// Link Data in d3 force format
  ///
  var force_links = raw_data.links.map((x) => (
    {
      source: x.endpoints[0].id, 
      target: x.endpoints[1].id,
      type: 'link'
    }
  ));
  console.log("force_links");
  console.log(force_links);

  var node_nodes = raw_data.nodes;

  var group_links = [];
  for(var i=0; i<raw_data.nodes.length; i++) {
    for(var j=0; j<raw_data.nodes[i].endpoints.length; j++) {
      group_links.push( {
        source: raw_data.nodes[i].endpoints[j],
        target: raw_data.nodes[i],
        type: 'group'
      });
    }
  }
  console.log("group_links");
  console.log(group_links);

  var endpoint_nodes = flatmap(raw_data.nodes, 
    (x) => x.endpoints.map((y) => { y.parent_props = x.props; return y; })
  );
  console.log("endpoint_nodes");
  console.log(endpoint_nodes);



  ///
  /// d3 init
  ///
  var container = document.getElementById("maindiv${divnum}");
  var canvas = document.createElement('canvas');
  canvas.id = 'theCanvas';
  canvas.width = width;
  canvas.height = height;
  container.appendChild(canvas);

  var cnvs_ = d3.select("canvas").call(d3.zoom().scaleExtent([-10,10]) .on("zoom", zoom))
      width = cnvs_.property("width"),
      height = cnvs_.property("height");




  var context = canvas.getContext("2d");
  var tfm = null;

  function zoom() {
    context.clearRect(0, 0, width, height)
    tfm = d3.event.transform;
    ticked(d3.event.transform)
  }


  var simulation = d3.forceSimulation()
    .force("link", 
      d3.forceLink()
      .id(function(d) { return d.id; })
      .distance(function(link) {
        if(link.type == 'group') {
          return 5;
        }
        else {
          return 50;
        }
      })
    )
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter())
    .stop();


  simulation
    .nodes([...endpoint_nodes, ...node_nodes]);
    //.on("tick", ticked);

  simulation.force("link")
    .links([...force_links, ...group_links]);


  var cnvs = d3.select("canvas");
  cnvs.on('click', () => {
    console.log("canvas click");
    var cxs = d3.mouse(cnvs.node());
    console.log(cxs);
    //var node = getNodeAtPoint(cxs[0] - width/2, cxs[1] - height/2);
    var node = getNodeAtPoint(cxs[0], cxs[1]);

  });

  for(i=0; i<100; i++) {
    simulation.tick()
  }

  ticked();



  //broken since zoom and pan
  function getNodeAtPoint(x_, y_) {

    var x = x_, y = y_;
    console.log(tfm);
    if(tfm != null) {
      var t = tfm.apply([x_, y_]);
      x = t[0]; 
      y = t[1];
    }

    for(i=0; i<endpoint_nodes.length; i++) {
      if (i >= node_nodes.length) {
        break;
      }
      var n = node_nodes[i];
      if(Math.abs(n.x - x) < 10 && Math.abs(n.y - y) < 10) {
        console.log(n.props.name);
        return n;
      }
    }

  }

  function ticked(T = d3.zoomIdentity) {

    T = T.translate(width/2.0, height/2.0);
    context.clearRect(0, 0, width, height);
    context.save();
    //context.translate(width / 2, height / 2);

    context.beginPath();
    force_links.forEach(x => drawLink(x,T));
    context.strokeStyle = "#22c";
    context.lineWidth = 2;
    context.stroke();

    context.beginPath();
    group_links.forEach(x => drawLink(x,T));
    context.strokeStyle = "#aaa";
    context.stroke();

    context.beginPath();
    endpoint_nodes.forEach(x => drawENode(x,T));
    context.fillStyle = "#aaa";
    context.fill();
    context.strokeStyle = "#aaa";
    context.stroke();

    context.beginPath();
    node_nodes.forEach(x => drawNode(x,T));
    context.fillStyle = "#111";
    context.fill();
    context.strokeStyle = "#111";
    context.stroke();

    context.restore();
  };

  function drawLink(d_, T) {
    ds = T.apply([d_.source.x, d_.source.y]);
    dt = T.apply([d_.target.x, d_.target.y]);
    context.moveTo(ds[0], ds[1]);
    context.lineTo(dt[0], dt[1]);
  }

  function drawENode(d_, T) {
    d = T.apply([d_.x, d_.y]);
    context.moveTo(d[0] + 3, d[1]);
    context.arc(d[0], d[1], 3, 0, 2 * Math.PI);
  }

  function drawNode(d_, T) {
    d = T.apply([d_.x, d_.y]);
    context.moveTo(d[0] + 7, d[1]);
    context.arc(d[0], d[1], 7, 0, 2 * Math.PI);
    context.fillStyle = "#eee";
    context.font = "1.6em monospace";
    context.fillText(d_.props.name, d[0] + 10, d[1] - 10);
  }
}
