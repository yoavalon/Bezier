d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)

d.end()
