d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.position_pen(2,0)

d.end()
