import {Edge} from './types'

function createEdge(from: number, to: number, cost: number) {
    return { from, to, cost };
}

/*
 *Bellman Ford algorithm
*/

/**
 *
 * @param edges List of edges
 * @param V number of verticies
 * @param start Starting position of the graph. Default is 0
*/
function bellmanFord(edges: Edge[], V: number, start = 0) {
  let distances: number[] = new Array(V).fill(Infinity);

  distances[start] = 0;

  for (let i = 0; i < V - 1; i++) {
    edges.forEach((edge) => {
      distances[edge.to] = Math.min(
        distances[edge.from] + edge.cost,
        distances[edge.to]
      );
    });
  }

  for (let i = 0; i < V - 1; i++) {
    edges.forEach((edge) => {
      if (distances[edge.from] + edge.cost < distances[edge.to]) {
        distances[edge.to] = Infinity * -1;
      }
    });
  }
  return distances;
}

let V = 10;
let edges: Edge[] = [
  createEdge(0, 1, 1),
  createEdge(1, 2, 1),
  createEdge(2, 4, 1),
  createEdge(3, 4, -3),
  createEdge(3, 2, 1),
  createEdge(1, 5, 4),
  createEdge(1, 6, 4),
  createEdge(5, 6, 5),
  createEdge(6, 7, 4),
  createEdge(5, 7, 3),
];

let distances = bellmanFord(edges, V);

distances.forEach((d, i) => console.log(`0 to ${i} the cost is ${d}`));