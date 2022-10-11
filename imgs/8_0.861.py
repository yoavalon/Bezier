d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SE, Length.medium)

d.end()
