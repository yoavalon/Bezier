d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,3)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
