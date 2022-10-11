d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.position_pen(0,0)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
