d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)

d.end()
