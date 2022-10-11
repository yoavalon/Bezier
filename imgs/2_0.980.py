d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
