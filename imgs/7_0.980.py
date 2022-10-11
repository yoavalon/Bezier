d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
