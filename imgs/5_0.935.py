d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)

d.end()
