d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
