d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)

d.end()
