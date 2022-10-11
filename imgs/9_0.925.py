d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
