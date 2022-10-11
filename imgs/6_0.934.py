d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.position_pen(2,0)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
