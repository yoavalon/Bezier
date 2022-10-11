d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
