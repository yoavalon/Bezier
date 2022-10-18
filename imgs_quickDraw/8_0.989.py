d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.position_pen(2,0)

d.end()
