d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)

d.end()
