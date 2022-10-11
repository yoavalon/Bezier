d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,2)

d.end()
