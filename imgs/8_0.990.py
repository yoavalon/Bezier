d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)

d.end()
