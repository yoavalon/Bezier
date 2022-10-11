d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,1)

d.end()
