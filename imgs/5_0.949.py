d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
