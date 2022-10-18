d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,0)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
