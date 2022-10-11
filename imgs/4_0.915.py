d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,0)
d.position_pen(1,0)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(2,1)

d.end()
