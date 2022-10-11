d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.position_pen(2,0)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.short)

d.end()
