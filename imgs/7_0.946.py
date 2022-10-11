d = DslBezier()

d.position_pen(2,1)
d.position_pen(2,0)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)

d.end()
