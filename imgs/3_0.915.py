d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.medium)

d.end()
