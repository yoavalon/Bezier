d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
