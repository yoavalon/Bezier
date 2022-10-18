d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)

d.end()
