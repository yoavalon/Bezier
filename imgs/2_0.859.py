d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,3)

d.end()
