d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.position_pen(3,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)

d.end()
