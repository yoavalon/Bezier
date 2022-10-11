d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,2)

d.end()
