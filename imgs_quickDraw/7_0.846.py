d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)

d.end()
