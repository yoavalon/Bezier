d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.long)

d.end()
