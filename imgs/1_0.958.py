d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)

d.end()
