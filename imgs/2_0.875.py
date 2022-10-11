d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)

d.end()
