d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)

d.end()
