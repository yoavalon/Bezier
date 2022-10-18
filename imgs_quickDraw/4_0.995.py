d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)

d.end()
