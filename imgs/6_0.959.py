d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
