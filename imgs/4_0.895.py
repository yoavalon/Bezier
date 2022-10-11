d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.position_pen(0,0)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,3)

d.end()
