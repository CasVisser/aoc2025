= Day 4

#let neighbors(x, y, rolls) = (
  (x + 1, y    ),
  (x + 1, y + 1),
  (x    , y + 1),
  (x - 1, y + 1),
  (x - 1, y    ),
  (x - 1, y - 1),
  (x    , y - 1),
  (x + 1, y - 1),
).filter(xy => xy in rolls)

#{
  let inp = read("4.in")

  // Parsing
  
  let width = inp.clusters().position(c => c == "\n")
  let height = inp.clusters().filter(c => c == "\n").len() + 1
  let rolls = inp
    .split("\n")
    .zip(range(height))
    .map(((line, y)) => 
      line
        .clusters() // as array of characters
        .zip(range(width))
        .filter(((c, _)) => c == "@")
        .map(((c, x)) => (x, y))
    )
    .join()

  // Algorithm
  
  let removed = ()
  let remaining_rolls = rolls
  while true {
    let removable = remaining_rolls
      .filter(xy => neighbors(..xy, remaining_rolls).len() < 4)
    if removable.len() == 0 { break }
    removed.push(removable)
    remaining_rolls = remaining_rolls.filter(xy => xy not in removed.join())
  }
  let part1 = removed.at(0).len()
  let part2 = removed.map(array.len).sum()

  // Visualization

  let c_empty = table.cell(fill: white, text(fill: luma(10%), ""))
  let c_roll(n: none) = {
    if n == none { return table.cell(fill: luma(10%), stroke: none, []) }
    
    let ratio = n / (removed.len() - 1) * 100%
    table.cell(
      fill: gradient.linear(..color.map.crest).sample(ratio), 
      stroke: 1.3pt + black,
      text(fill: white, [*#(n + 2)*]) // number the 1st round of removals as 1, not as 0
    )
  }

  let cells = range(height)
    .map(y => range(width)
      .map(x => {
        if (x, y) not in rolls { c_empty }
        else if (x, y) not in removed.join() { c_roll() }
        else {
          let removed_in_round = removed
            .zip(range(removed.len()))
            .filter(((xys, _)) => (x, y) in xys)
            .first().last()
          c_roll(n: removed_in_round)
        }
      }))
    .join()

  table(
    columns: (2.2em,) * width,
    rows: (2.2em,) * height,
    stroke: luma(40%),
    align: center + horizon,
    ..cells
  )

  [
    Part 1: #part1 \
    Part 2: #part2 \
  ]
}

