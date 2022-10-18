d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
