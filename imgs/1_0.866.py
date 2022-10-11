d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)

d.end()
