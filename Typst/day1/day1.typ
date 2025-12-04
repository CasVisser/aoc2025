#let pad(x, width) = {
  let s = str(x)
  " " * (width - s.len()) + s
}

#let show_dial(n) = {
  let dial = circle(radius: 9pt)[
    #set align(center + bottom)
    #emoji.arrow.t.filled \
    #v(2pt)
  ]
  rotate((n / 100) * 360deg, dial)
}

#let values = ()
#{
  let inp = read("1.in")
  let lines = inp.split("\n")
  let part1 = 0
  let part2 = 0
  let dial = 50
  let inital_values = ("", dial, part1, part2, show_dial(dial))
  values.push(inital_values)
  
  
  for line in inp.split("\n") {
    let direction = line.at(0)
    let amount = int(line.slice(1))

    if direction == "R" {
      part2 += calc.quo(dial + amount, 100)
      dial = calc.rem-euclid((dial + amount), 100)
    }
    else if direction == "L" {
      part2 += calc.quo(calc.rem(100 - dial, 100) + amount, 100)
      dial = calc.rem-euclid((dial - amount), 100)
    }
    if dial == 0 {part1 += 1}
    
    values.push((direction + pad(amount, 3), dial, part1, part2, show_dial(dial)))
  }
}

= Day 1

#show table.cell.where(y: 0): set text(white, weight: "bold")
#set table(
  align: (x, y) => {
    if y == 0 {return left + horizon}
    if x == 4 {return center + horizon}
    return right + horizon
  },
  fill: (_, y) => {
    if y == 0 {luma(30%)}
  }
)

#table(
  columns: (auto,) * 5,
  rows: 2.2em,
  table.header[Instruction][Dial][Part 1][Part 2][Vis.],
  ..values.flatten().map(it => [#it])
)
