d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,3)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)

d.end()
