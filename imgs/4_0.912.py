d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.position_pen(2,3)

d.end()
