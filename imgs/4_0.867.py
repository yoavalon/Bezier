d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)

d.end()
