d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)

d.end()
