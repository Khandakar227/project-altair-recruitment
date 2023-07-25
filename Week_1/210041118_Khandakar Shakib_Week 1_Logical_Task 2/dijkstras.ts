import {Edge} from './types'

/**
 * Edges from and to must be in incremental order.
 * Example: createEdge(0, 1, 5) is Ok.
 *          createEdge(1, 0, 5) is not Ok.
 */
function createEdge(from: number, to: number, cost: number) {
    return { from, to, cost };
}


/*
 * Dijkstra's Algorithm
 * For Undirected graphs
*/
function dijkstra(edges: Edge[], V: number, start = 0) {
    let distances: number[] = new Array(V).fill(Infinity);
    let paths:String[] = new Array(V).fill("");
    distances[start] = 0;
    paths[0] = " ";
    
    for (let i = 0; i < edges.length; i++) {
      if (distances[edges[i].from] + edges[i].cost < distances[edges[i].to]) {
          distances[edges[i].to] = distances[edges[i].from] + edges[i].cost;
          paths[edges[i].to] = paths[edges[i].from];
          paths[edges[i].to]+=edges[i].from + " ";
      }
        if (distances[edges[i].from] === Infinity && distances[edges[i].to] !== Infinity)
        {
            distances[edges[i].from] = distances[edges[i].to] + edges[i].cost;
            paths[edges[i].from] = paths[edges[i].to];
            paths[edges[i].from]+=edges[i].to + " ";
        }
    }
    distances.forEach((d, i) => console.log(`Shortest Distance from starting point to node ${i} is ${d}`));
    paths.forEach((p, i) => console.log(`Shortest path to ${i} is ${p.trim().replace(/ /g, "->")}`))
  }


  let V =8
  let edges:Edge[] = [
      createEdge(0, 1, 1),
      createEdge(1, 2, 1),
      createEdge(2, 4, 1),
      createEdge(3, 4, 3),
      createEdge(2, 3, 1),
      createEdge(1, 5, 4),
      createEdge(1, 6, 4),
      createEdge(5, 6, 5),
      createEdge(6, 7, 4),
      createEdge(5, 7, 3),
    ];
  
  dijkstra(edges, V);