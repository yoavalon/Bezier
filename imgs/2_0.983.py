d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.medium)

d.end()
