d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.long)
d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)

d.end()
