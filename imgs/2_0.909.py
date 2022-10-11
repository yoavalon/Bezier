d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,0)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,3)

d.end()
