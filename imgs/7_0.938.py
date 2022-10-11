d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
