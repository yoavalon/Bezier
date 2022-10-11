d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,2)

d.end()
