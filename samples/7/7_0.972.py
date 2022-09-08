d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.position_pen(2,3)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.low)

d.end()
