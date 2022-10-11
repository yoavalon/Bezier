d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.position_pen(1,2)

d.end()
